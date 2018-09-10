import APICallbacklogin from './utils_login';

let logInPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.108:8000/login/';	
	return APICallbacklogin(dataToSend, endPointAPI, method, successStateCode);
}

export default logInPostAPI;