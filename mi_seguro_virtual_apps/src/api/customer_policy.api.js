import APICallback from './utils';

let CustomerPolicyPostAPI = (dataToSend,token) => {
	let method = "GET", successStateCode = 200 ;
	let endPointAPI = 'http://192.168.0.21:8000/customer/policy/detail/';
	return APICallback(dataToSend, endPointAPI, method, successStateCode,token);
}

export default CustomerPolicyPostAPI;