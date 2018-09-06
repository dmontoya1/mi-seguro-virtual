APICallback = (dataToSend, endPointAPI, method, successStateCode) => {
	let keys = Object.keys(dataToSend);

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

	let options = {
		method,
		headers: {
			'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMywidXNlcm5hbWUiOiJNYXJpb0BwcnVlYmEuY29tIiwiZXhwIjoxNTM2Mjc3MDY3LCJlbWFpbCI6Ik1hcmlvQHBydWViYS5jb20ifQ.Dekur-xHUZLOlMas4ojre9zYmtO8k9ZvnA4SJC8aQ08',
			'Accept': 'application/json',
			'Content-Type': 'application/json',
		}
	};

	if (method != "GET") {
		options.body = body;
	}

	return fetch(`${endPointAPI}${urlParams}`, options)
		.then((response) => {
			return {
				errored: response.status != successStateCode,
				status: response.status,
				data: response.json()
			}
		});
}


export default APICallback;