import APICallback from './utils';

let InsurancePostAPI = (dataToSend,token) => {
	let method = "GET", successStateCode = 200 ;
	let endPointAPI = 'api/insurances/insurance/detail/';
	return APICallback(dataToSend, endPointAPI, method, successStateCode,token);
}

export default InsurancePostAPI;