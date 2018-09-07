import APICallback from './utils';

let InsurancePostAPI = (dataToSend,token) => {
	let method = "GET", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.21:8000/seguro/detail/';
	console.warn("token en el callback",token);	
	return APICallback(dataToSend, endPointAPI, method, successStateCode,token);
}

export default InsurancePostAPI;