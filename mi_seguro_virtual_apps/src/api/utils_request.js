APICallbackRequest = (dataToSend, endPointAPI, method, successStateCode, token, photo1, photo2) => {
	let keys = Object.keys(dataToSend);
	let api_url = 'http://192.168.0.18:8000';
	var urlParams = '';

	for (var i = 0; i < keys.length; i++) {
		let key = keys[i];
		let value = `${dataToSend[key]}`.replace(" ", "%20");
		value = `${dataToSend[key]}`.replace("#", "nro");

		if (i !== 0) urlParams += `&`;
		else urlParams += `?`;

		urlParams += `${key}=${value}`;
	}

	let body = new FormData();
	body.append('name', dataToSend.name);
	body.append('adviser_code', dataToSend.adviser_code);
	body.append('photo1', {
    uri: photo1,
    type: 'image/jpeg', // or photo.type
    name: 'foto_tarjeta'
  	});
  	body.append('photo2', {
    uri: photo2,
    type: 'image/jpeg', // or photo.type
    name: 'foto_licencia'
  	}); 
  	
	let jwt = 'JWT '

	let options = {
		method,
		headers: {
			'Authorization': `${jwt}${token}`,
			'Accept': 'application/json',
			'Content-Type': 'multipart/form-data',
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


export default APICallbackRequest;