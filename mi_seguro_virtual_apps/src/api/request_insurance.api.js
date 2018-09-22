import APICallbackRequest from './utils_request';

let RequestInsurancePostAPI = (dataToSend, token, photo1, photo2) => {
    let method = "POST", successStateCode = 200 ;
	let endPointAPI = 'insurance/request/';
	return APICallbackRequest(dataToSend, endPointAPI, method, successStateCode,token, photo1.uri, photo2.uri);
}

export default RequestInsurancePostAPI;