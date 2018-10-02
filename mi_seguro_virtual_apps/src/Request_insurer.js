import React, { Component } from 'react';
import { Accordion, Content, Container, Header, Left, Body, Right, Button, Icon, Card, CardItem, View, Text, Form, Input, Item } from 'native-base';
import { Image, StyleSheet,TouchableOpacity, Alert } from 'react-native';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';

import { Actions } from 'react-native-router-flux';


import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

import ImagePicker from 'react-native-image-picker';

import RequestInsurancePostAPI from '././api/request_insurance.api';

export default class Request extends Component {

    state = {
      token:'',
      image1: null,
      image2: null,
      button_photo1:false,
      button_photo2:false,
      adviser_code:''
    };

  submit(){
    if (this.state.image1 == null || this.state.image2 == null){
      Alert.alert(
        'Atención',
        'Debes cargar las fotografias requeridas.',
        [
          {text: 'OK', onPress: () => console.log('OK Pressed')},
        ],
        { cancelable: false }
      )
    }else{
      console.warn("bueno");
    }
  }
  

  selectPhotoTapped = () => {
    const options = {
      title: 'Tomar una foto',
      takePhotoButtonTitle: 'Tomar una foto',
      chooseFromLibraryButtonTitle: 'Seleccionar una foto',
      cancelButtonTitle: 'CANCELAR',
      quality: 1.0,
      storageOptions: {
        skipBackup: true
      }
    };

    ImagePicker.showImagePicker(options, (response) => {

      if (response.didCancel) {
        Alert.alert(
          'Atención',
          'Usuario cancelo la captura de foto.',
          [
            {text: 'OK', onPress: () => console.log('OK Pressed')},
          ],
          { cancelable: false }
        )
      }
      else if (response.error) {
        Alert.alert(
          'Error',
          'Error al cargar la foto.',
          [
            {text: 'OK', onPress: () => console.log('OK Pressed')},
          ],
          { cancelable: false }
        )
      }
      else if (response.customButton) {
        console.warn('User tapped custom button: ', response.customButton);
      }
      else {
        let source = { uri: response.uri };
        this.setState({
          image1: source,
          button_photo1:true
        });
      }
    });
  }

  selectPhotoTapped2 = () => {
    const options = {
      title: 'Tomar una foto',
      takePhotoButtonTitle: 'Tomar una foto',
      chooseFromLibraryButtonTitle: 'Seleccionar una foto',
      cancelButtonTitle: 'CANCELAR',
      quality: 1.0,
      storageOptions: {
        skipBackup: true
      }
    };

    ImagePicker.showImagePicker(options, (response) => {

      if (response.didCancel) {
        Alert.alert(
          'Atención',
          'Usuario cancelo la captura de foto.',
          [
            {text: 'OK', onPress: () => console.log('OK Pressed')},
          ],
          { cancelable: false }
        )
      }
      else if (response.error) {
        Alert.alert(
          'Error',
          'Error al cargar la foto.',
          [
            {text: 'OK', onPress: () => console.log('OK Pressed')},
          ],
          { cancelable: false }
        )
      }
      else if (response.customButton) {
        console.warn('User tapped custom button: ', response.customButton);
      }
      else {
        let source = { uri: response.uri };
        this.setState({
          image2: source,
          button_photo2:true
        });
      }
    });
  }


  _menu = null;

  setMenuRef = ref => {
    this._menu = ref;
  };

  hideMenu = () => {
    this._menu.hide();
  };

  showMenu = () => {
    this._menu.show();
  };

  submit(){
    let name = this.props.seguro[0].name;
    let adviser_code = this.state.adviser_code;
    let dataToSend = {
        name,
        adviser_code
    };
    let token = this.props.token;
    if (this.state.image1 != null && this.state.image2 != null){
        RequestInsurancePostAPI(dataToSend, token, this.state.image1, this.state.image2).then(data => { 
        if (data.errored){
          console.warn(data);
        } else {
            Alert.alert(
            'Información',
            "Solicitud realizada con exito.",
            [
              {text: 'Aceptar', onPress:() => Actions.home({token: token})},
            ],
            { cancelable: false }
          )
        }

      }); 
    } else {
      Alert.alert(
        'Error',
        "Por favor adjuntar las imagines requeridas para realizar la solicitud.",
        [
          {text: 'Aceptar', onPress: () =>{}},
        ],
        { cancelable: false }
      )
    }
    
  }



  render() {
    let token = this.props.token;
    const image1 = require('../assets/icons/camara.png');
    const image2 = require('../assets/icons/check.png');  
    let url;
    if (!this.state.button_photo1) {
        url = image1
    } else if(this.state.button_photo1) {
        url = image2
    }
    if (!this.state.button_photo2) {
      url2 = image1
    } else if(this.state.button_photo2) {
      url2 = image2
    }
    return (
      <Container style={{paddingTop:20}}>
        <Header style={styles.container}>
          <Left>
            <Button transparent onPress={() => Actions.pop()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body style={{position: 'absolute', left: wp('30%')}}>
            <Image 
                source={require('../assets/images/logo.png')}
                resizeMode='contain' 
                style={{width:150, height:30}}
            />
          </Body>
          <Right>
          <Menu
            ref={this.setMenuRef}
            button={<Button
                        transparent 
                        onPress={this.showMenu}
                        style={{width:70, height:70}} 
                    >
                      <Image
                        source={require('../assets/icons/cuenta.png')} 
                        resizeMode='contain' 
                        style={{width:50, height:50}} 
                      /> 
                    </Button>
                  }
          >
            <MenuItem onPress={() => {}}>Perfil</MenuItem>
            <MenuItem onPress={() => Actions.logIn()}>Cerrar sesión</MenuItem>
          </Menu>   
          </Right>    
        </Header>
        <View style={{paddingTop:10, paddingLeft:5}}>
            <Card style={{width: wp('96%')}}>
                <CardItem>
                <View style={{flex:1}}>
                    <View style={{flexDirection: 'row', width:wp('75%')}}>
                        <View style={{position:'relative', top:-5, right:10}}>
                            <Image 
                                source={require('../assets/icons/Scellphone.png')}
                                resizeMode='contain' 
                                style={{width:40, height:40, opacity:0.38}}
                            />
                        </View>
                        <View>
                            <Text style={{color:'rgba(0,0,0,0.4)', fontSize:13, paddingLeft:10}}>
                                Ahora podrás llevar tu SOAT en tu celular y presentarlo cuando lo requieras.
                            </Text>
                        </View>
                    </View>
                    <View style={{flexDirection: 'row', width:wp('75%'), paddingTop:20}}>
                        <View style={{position:'relative', top:-5, right:5}}>
                            <Image 
                                source={require('../assets/icons/call.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38}}
                            />
                        </View>
                        <View>
                            <Text style={{color:'rgba(0,0,0,0.4)', fontSize:13, paddingLeft:20}}>
                                En caso de requerir asistencua puedes comunicarte con nosotros.
                            </Text>
                        </View>
                    </View>
                  </View>
                </CardItem>
              </Card>
              <Card style={{width: wp('96%')}}>
                <CardItem style={{ width:wp('90%'), position:'relative', left:10}}>
                <View style={{paddingTop:20, flex:1}}>
                    <View style={{flexDirection: 'row'}}>
                        <View>
                            <Text style={{color:'rgba(0,0,0,1)', fontSize:13, position:'relative', top:-5, right:10}}>
                                Forografía de tu tarjeta de propiedad.
                            </Text>
                        </View>
                        <View style={{position:'relative', top:-15, left:wp('11%')}}>
                            <Button transparent onPress={this.selectPhotoTapped}>
                            <Image 
                                source={url}
                                style={{width:40, height:40}}

                            />
                            </Button>
                        </View>
                    </View>
                    <View style={{flexDirection: 'row', paddingTop:20}}>
                        <View>
                            <Text style={{color:'rgba(0,0,0,1)', fontSize:13, position:'relative', top:-5, right:10}}>
                                Fotografía de tu licencia de conducción.
                            </Text>
                        </View>
                        <View style={{position:'relative', top:-15, left:wp('5%')}}>
                        <Button transparent onPress={this.selectPhotoTapped2}>
                            <Image 
                                    source={url2}
                                    style={{width:40, height:40}}
                                />
                        </Button>
                        </View>
                    </View>
                  </View>
                </CardItem>
            </Card>
            <Card>
              <CardItem>
                  <Input 
                    placeholder='Codigo Asesor'
                    placeholderTextColor='rgba(0,0,0,0.4)'
                    onChangeText={(adviser_code) => this.setState({adviser_code})} />
              </CardItem>
            </Card>
            <View style={{paddingLeft:10,paddingRight:10, paddingTop:30}}>
              <Button block danger style={styles.button} onPress={() => this.submit(this.state.image1,this.state.image2)}>
                  <Text style={{color:'white'}}>SOLICITAR</Text>
              </Button>
            </View>
        </View>
      </Container>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    backgroundColor: '#05071e',
    paddingTop:20
  },
  button: {
    borderRadius: 10,
},
});