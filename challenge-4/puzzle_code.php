<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
	<head>
		<title>Jean Gourd - Wondering What To Do With The Code?</title>
		<style type="text/css">@import url(/global.css);</style>
		<meta name="robots" content="noindex"/>
	</head>
	<body>
		<!--
		/************************************************************************
		 * Copyright (c) 2007-2018, Jean Gourd                                  *
		 * www.jeangourd.com                                                    *
		 *                                                                      *
		 * Please feel free to use any of my code (JavaScript, PHP, CSS) in     *
		 * your web documents.  I only ask that you leave my copyright notice   *
		 * within your source.  Hey, it's not such a huge thing to ask, right?  *
		 ************************************************************************
		 * This file is part of www.jeangourd.com.                              *
		 *                                                                      *
		 * Any JavaScript, PHP, or CSS code contained herein is free software;  *
		 * you can redistribute it and/or modify it under the terms of the GNU  *
		 * General Public License as published by the Free Software Foundation; *
		 * either version 2 of the License, or (at your option) any later       *
		 * version.                                                             *
		 *                                                                      *
		 * This is distributed in the hope that it will be useful, but WITHOUT  *
		 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY   *
		 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public     *
		 * License for more details.                                            *
		 *                                                                      *
		 * To obtain a copy of the GNU General Public License, write to the     *
		 * Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,         *
		 * Boston, MA 02110-1301 USA                                            *
		 ************************************************************************/
		-->
		<div id="header">
			<img class="image" src="/images/pixel.gif" width="100" height="1" alt="monkey logo"/> Jean Gourd<span class="image">&nbsp;</span><img class="image" src="/images/the_dude.jpg" width="100" height="93" alt="the dude"/>
		</div>
		<div class="bar top_bar">
			<div class="bar_section bar_section_50 bar_section_left">
				Optimized for <a href="http://www.google.com/intl/en/chrome/">Google Chrome</a> <span class="bar_hidden_text">...because Internet Explorer sucks donkey balls</span>
			</div>
			<div class="bar_section bar_section_50 bar_section_right">
				<a href="javascript: history.go(-1);">Back</a> | <a href="/">Home</a>
			</div>
		</div>

		<div id="middle">
			<h1>Wondering What To Do With The Code?</h1>
			<div class="body">
				Find three (3) ways to make the program you decrypted output a hyphen "<code>-</code>" 20 times in succession by changing or adding only one character to the code.  So the output will look like this: <code>--------------------</code>.<p/>

				NOTES:<p/>
				<ol>
					<li>You may not at any time remove a character from the code.</li>
					<li>You may change a single character in the code or you may add a single character to the code--but not both at any one time.</li>
					<li>Once you've found a solution (that compiles and produces the specified output), you must change the code back to its original state before attempting another solution; this probably means that you should save an extra copy of the code to use as a reference.</li>
					<li>The code in question begins at "<code>{</code>" and ends at "<code>}</code>".</li>
				</ol><p/>

				An example: changing <code>i&lt;n</code> to <code>~i&lt;n</code> will output 21 hyphens in succession.  Note that this is not a solution; it is only an example of a valid modification to the code (i.e., a single character was added).<p/>

				What next?  Once you've successfully obtained all three solutions, you must now:<p/>

				<ol>
					<li>Isolate the three new characters (whether added or changed).</li>
					<li>Sort them in increasing order according to their ASCII value.</li>
					<li>Generate a bit string representing the three characters.  The bit string you generate is your password.  Use it to help you solve other parts of the puzzle that appear later.  In the meantime, <a href="puzzle_missing_letters.php">check this out</a>.</li>
				</ol><p/>

				An example: let's say that you solved the puzzle three separate times by 1) adding a <code>~</code> before the condition <code>i&lt;n</code> in the for loop statement (i.e., as in the example above), 2) changing the <code>2</code> to a <code>4</code> in the declaration and initialization of <code>n</code>, and 3) changing the <code>0</code> to a <code>1</code> in the for loop initial assignment of <code>i</code>.<p/>

				The three new characters you have obtained as a result of making changes and/or additions are <code>~</code>, <code>4</code>, and <code>1</code>.  The ASCII value of <code>~</code> is 126, of <code>4</code> is 52, and of <code>1</code> is 49.  In increasing order, the characters would be sorted as <code>14~</code> which corresponds to the decimal ASCII values 49, 52, and 126.  Each ASCII value can be represented with 7 bits, so our final bit string is <code>011000101101001111110</code>.  It might be good to remember this <b>b</b>it <b>s</b>tring.
			</div>
		</div>

		<div class="bar bottom_bar">
			<div class="bar_section bar_section_75 bar_section_left">
				<a href="/quote.php?num=11">A&nbsp;day&nbsp;without&nbsp;sunshine&nbsp;is&nbsp;like,&nbsp;well,&nbsp;night.</a>
			</div>
			<div class="bar_section bar_section_25 bar_section_right">
				Last updated: 2019-03-07 11:14
			</div>
		</div>
		<div id="footer">
			Copyright (c) 2007-2019, Jean Gourd<br/><br/>
			Have any funny quotes?  <a href="#email" onclick="this.href='amliotj:ogru[dtal]tace[hod]tdeu'.replace(/(.)(.)/g, '$2$1').replace(/\[at\]/g, '@').replace(/\[dot\]/g, '.');">I would love to hear them</a>!<br/>
			Please <a href="#email" onclick="this.href='amliotj:ogru[dtal]tace[hod]tdeu'.replace(/(.)(.)/g, '$2$1').replace(/\[at\]/g, '@').replace(/\[dot\]/g, '.');">report broken links</a>.<br/><br/>
			Jean Gourd, Ph.D.<br/>
			Associate Professor of Computer Science<br/>
			College of Engineering and Science<br/>
			Louisiana Tech University<br/>
			P.O. Box 10348<br/>
			Ruston, LA 71272<br/>
			Voice: 318.257.4301<br/>
			Fax: 318.257.4922<br/>
			<a href="#email" onclick="this.href='amliotj:ogru[dtal]tace[hod]tdeu'.replace(/(.)(.)/g, '$2$1').replace(/\[at\]/g, '@').replace(/\[dot\]/g, '.');"><script type="text/javascript">document.write('gjuodra[]talethcd[toe]ud'.replace(/(.)(.)/g, '$2$1').replace(/\[at\]/g, '@').replace(/\[dot\]/g, '.'));</script></a><br/>
			<a href="/">www.jeangourd.com</a><br/>
<!--			<a href="http://www.wunderground.com/wundermap/?lat=32.45416&lon=-92.67517&zoom=8&type=ter&units=english&rad=1&rad.num=6&rad.spd=25&rad.opa=70&rad.stm=0&rad.type=N0R&rad.type2=&rad.smo=1&rad.mrg=0&wxsn=0&svr=0&cams=0&sat=0&riv=0&mm=0&hur=0&fire=0&tor=0&ndfd=0&pix=0&dir=0&ihg=0">Situational Awareness</a>-->
<!--			<a href="http://www.wunderground.com/wundermap/?lat=32.45416&lon=-92.67517&zoom=8&type=ter&units=english&rad=1&rad.num=6&rad.spd=25&rad.opa=70&rad.stm=0&rad.type=N0R&rad.type2=&rad.smo=1&rad.mrg=0&wxsn=0&svr=0&cams=0&sat=0&riv=0&mm=0&hur=0&fire=0&tor=0&ndfd=0&pix=0&dir=0&ads=0&hd=0&ib=0">Situational Awareness</a>-->
			<a href="http://wxug.us/22ke4">Situational Awareness</a>

		</div>
		<script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
		<script type="text/javascript">
		<!--
			_uacct = "UA-1558559-1";
			urchinTracker();
		// -->
		</script>
	</body>
</html>
