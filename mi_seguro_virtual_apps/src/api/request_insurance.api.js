import APICallback from './utils';

let RequestInsurancePostAPI = (dataToSend,token) => {
    let method = "POST", successStateCode = 200 ;
    console.warn(token);
	let endPointAPI = 'http://192.168.0.21:8000/insurance/request/';
	return APICallback(dataToSend, endPointAPI, method, successStateCode,token);
}

export default RequestInsurancePostAPI;