import APICallback from './utils';

let signUpPostAPI = (dataToSend) => {
	let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.108:8000/sign_up/';	
	return APICallback(dataToSend, endPointAPI, method, successStateCode);
}

export default signUpPostAPI;