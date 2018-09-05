import APICallback from './utils';

let logInPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.21:8000/api-token-auth/';	
	return APICallback(dataToSend, endPointAPI, method, successStateCode);
}

export default logInPostAPI;