from flask import Flask, jsonify, request, render_template, send_file
import subprocess
import json
import os
import inspect
import sys
import time
import codecs
import commands

dir_path = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
sys.path.append(dir_path+"/../")

flite_bin = "flite"
output_common = dir_path+"/output/"
voice = dir_path+"/voices/"
start_file_name = 0001

# Setup flask app
flask_app = Flask(__name__)

supported_voices = {
	"english": "",
	"hindi": voice+"cmu_indic_axb_hi.flitevox",
	"tamil": voice+"cmu_indic_sxv_ta.flitevox",
	"telugu": voice+"cmu_indic_knr_te.flitevox",
	"marathi": voice+"cmu_indic_slp_mr.flitevox"
}

output_dirs = {
	"english": output_common+"/english/",
	"hindi": output_common+"/hindi/",
	"tamil": output_common+"/tamil/",
	"telugu": output_common+"/telugu/",
	"marathi": output_common+"/marathi/"
}

@flask_app.route('/')
def index():
    return 'Index Page'

@flask_app.route("/download/",methods=['POST'])
def download():
	req_json = json.loads(request.data)
	filename = req_json['filename']
	la = filename.split("_")[0]
	try:
		# return send_file(output_dirs[la]+filename,attachment_filename=filename)
		return send_file(
			output_dirs[la] + filename,
			mimetype="audio/wav",
			as_attachment=True,
			attachment_filename=filename)
	except Exception as e:
		return str(e)

@flask_app.route("/tts/",methods=['POST'])
def text_to_speech():
	req_json = json.loads(request.data)
	text = req_json['input']
	la = req_json['language']

	response = {}
	if la in supported_voices.keys():
		files = os.listdir(output_dirs[la])
		filename = la + "_"
		file_len = len(files)
		if file_len == 0:
			filename = filename + str(start_file_name)+".wav"
		elif file_len >= 1:
			count = start_file_name + file_len
			filename = filename + str(count)+".wav"

		print filename
		failed = False
		try:
			print(output_dirs[la]+filename)
			arg_1 = u" -t \"" + unicode(text)+"\""
			arg_3 = u" -o " + unicode(output_dirs[la]+filename)
			if supported_voices[la] != "":
				arg_2 = u" -voice " + unicode(supported_voices[la])
				args = arg_1 + arg_2 + arg_3
			else:
				args = arg_1 + arg_3
			cmd = flite_bin + args

			wr = codecs.open(dir_path+"/shell_command.sh","w","utf-8")
			wr.write(cmd)
			wr.close()
			os.system("sudo bash shell_command.sh")
			time.sleep(3)
			os.remove(dir_path+"/shell_command.sh")
		except Exception as e:
			print(e)
			response['status'] = "failure"
			response['output_file'] = ""
			response["message"] = e.message
			response['language'] = la
			failed = True

		if not failed:
			response['status'] = "success"
			response['output_file'] = filename
			response["message"] = "success"
			response['language'] = la

	else:
		response['status'] = "failure"
		response["message"] = "unsupported languages"
		response['output_file'] = ""
		response['language'] = la

	return jsonify(response)

