import APICallbacklogin from './utils_login';

let logInPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'api/users/login/';	
	return APICallbacklogin(dataToSend, endPointAPI, method, successStateCode);
}

export default logInPostAPI;