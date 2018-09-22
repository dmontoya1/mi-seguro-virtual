import APICallbacklogin from './utils_login';

let logInPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'login/';	
	return APICallbacklogin(dataToSend, endPointAPI, method, successStateCode);
}

export default logInPostAPI;