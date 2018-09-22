import APICallbacklogin from './utils_login';

let signUpPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'sign_up/';	
	return APICallbacklogin(dataToSend, endPointAPI, method, successStateCode);
}

export default signUpPostAPI;