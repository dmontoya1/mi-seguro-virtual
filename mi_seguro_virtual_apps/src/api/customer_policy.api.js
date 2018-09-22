import APICallback from './utils';

let CustomerPolicyPostAPI = (dataToSend,token) => {
	let method = "GET", successStateCode = 200 ;
	let endPointAPI = 'api/insurances/customer/policy/detail/';
	return APICallback(dataToSend, endPointAPI, method, successStateCode,token);
}

export default CustomerPolicyPostAPI;