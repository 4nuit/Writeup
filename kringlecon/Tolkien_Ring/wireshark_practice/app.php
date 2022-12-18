<script>

	let d = -new Date().getTimezoneOffset();
	let n = Intl.DateTimeFormat().resolvedOptions().timeZone;

	function set_cookie (name, value, minutes) {
	  
		let date = new Date();
		date.setTime(date.getTime() + (minutes * 60 * 1000));
		
		let expires = "";
		
		if (minutes)
			expires = "; expires="+date.toGMTString();
			
		document.cookie = name + "=" + escape (value) + expires+";path=/";   
	}

	function get_cookie (cookie_name) {
	  let results = document.cookie.match ('(^|;) ?' + cookie_name + '=([^;]*)(;|$)');
	 
	  if (results)
		return (unescape (results[2]));
	  else
		return null;
	}

	if (!get_cookie('d') && !get_cookie('n')) {
		set_cookie('d', d, 2);
		set_cookie('n', n, 2);
		document . location . reload();
	}

	</script>