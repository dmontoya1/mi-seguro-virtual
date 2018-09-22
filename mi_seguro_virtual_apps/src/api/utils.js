APICallback = (dataToSend, endPointAPI, method, successStateCode,token) => {
	let keys = Object.keys(dataToSend);
	let api_url = 'http://192.168.0.21:8000';
	var urlParams = '';

	for (var i = 0; i < keys.length; i++) {
		let key = keys[i];
		let value = `${dataToSend[key]}`.replace(" ", "%20");
		value = `${dataToSend[key]}`.replace("#", "nro");

		if (i !== 0) urlParams += `&`;
		else urlParams += `?`;

		urlParams += `${key}=${value}`;
	}


	let body = JSON.stringify(dataToSend);
	let jwt = 'JWT '

	let options = {
		method,
		headers: {
			'Authorization': `${jwt}${token}`,
			'Accept': 'application/json',
			'Content-Type': 'application/json',
		}
	};

	if (method != "GET") {
		options.body = body;
	}

	return fetch(`${api_url}/${endPointAPI}${urlParams}`, options)
		.then((response) => {
			return {
				errored: response.status != successStateCode,
				status: response.status,
				data: response.json()
			}
		});
}


export default APICallback;