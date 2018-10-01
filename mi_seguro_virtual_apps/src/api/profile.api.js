import APICallback from './utils';

let ProfileGetApi = (dataToSend,token) => {
	let method = "GET", successStateCode = 200 ;
	let endPointAPI = 'api/users/customer/';
	return APICallback(dataToSend, endPointAPI, method, successStateCode, token);
}

export default ProfileGetApi;