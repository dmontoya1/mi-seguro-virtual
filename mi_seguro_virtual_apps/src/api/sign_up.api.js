import APICallbacklogin from './utils_login';

let signUpPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.10:8000/api/users/sign_up/';
	return APICallbacklogin(dataToSend, endPointAPI, method, successStateCode);
}

export default signUpPostAPI;