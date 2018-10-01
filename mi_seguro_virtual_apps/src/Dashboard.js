import React, { Component } from 'react';

import { 
    Accordion,
    Content,Footer, 
    FooterTab, 
    Container, 
    Header, 
    Left, 
    Body, 
    Right, 
    Button, 
    Icon, 
    Card, 
    CardItem, 
    View, 
    Text 
} from 'native-base';


import{
    Image,
    StyleSheet,
    TouchableHighlight,
    Animated,
    Alert
} from 'react-native';

import Modal from 'react-native-root-modal';

import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

import { Actions } from 'react-native-router-flux';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';

import InsurancePostAPI from '././api/insurance.api';
import CustomerPolicyPostAPI from '././api/customer_policy.api';
import ProfileGetApi from '././api/profile.api';


export default class Dashboard extends Component {

    constructor(props) {
    super(props);
        this.state = {
            token: '',
            visible: false,
            scale: new Animated.Value(1),
            x: new Animated.Value(0)
        };
        this.request = this.request.bind(this);
        this.requestPolicy = this.requestPolicy.bind(this);
        this.getProfile = this.getProfile.bind(this);
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

    scaleModal = () => {
        this.state.x.setValue(0);
        this.state.scale.setValue(0);
        Animated.spring(this.state.scale, {
            toValue: 1
        }).start();
        this.setState({
            visible: true
        });
        this.slide = false;
    };

    hideModal = () => {
        if (this.slide) {
            Animated.timing(this.state.x, {
                toValue: -320
            }).start(() => {
                this.setState({
                    visible: false
                });
            });
        } else {
            Animated.timing(this.state.scale, {
                toValue: 0
            }).start(() => {
                this.setState({
                    visible: false
                });
            });
        }

    };

    request(){
        let name = 'SOAT';
        let dataToSend = {
            name
        };
        let token = this.props.token;
        InsurancePostAPI(dataToSend,token).then(data => {
            if (data.errored){
              Alert.alert(
                'Error',
                "error.",
                [
                  {text: 'Aceptar', onPress: () =>{}},
                ],
                { cancelable: false }
              ) 
            } else {
                let seguro = (data.data._55.details)
                Actions.request({seguro: seguro, token: token});
            }
    
          });
    }
    requestPolicy(){
        let dataToSend = {};
        let token = this.props.token;
        CustomerPolicyPostAPI(dataToSend,token).then(data => {
            if (data.errored){
              Alert.alert(
                'Atención',
                "Aún no tienes pólizas creadas. Puedes crear una desde aquí",
                [
                  {text: 'Aceptar', onPress: () =>{}},
                ],
                { cancelable: false }
              ) 
            } else {
                let policy = (data.data._55.details)
                Actions.insurance({policy: policy, token: token});
            }
    
          });
    }
    getProfile(){
        let dataToSend = {};
        let token = this.props.token;
        ProfileGetApi(dataToSend,token).then(data => {
            if (data.errored){
              Alert.alert(
                'Atención',
                "Ha ocurrido un error al ingresar a tu perfil",
                [
                  {text: 'Aceptar', onPress: () =>{}},
                ],
                { cancelable: false }
              ) 
            } else {
                let profile = (data.data._55)
                Actions.profile({profile: profile, token: token});
            }
    
          });
    }

    render() {
        let token = this.props.token;
        return (  
        <Container>
            <View style={styles.container}>
                <Animated.Modal
                    visible={this.state.visible}
                    style={[styles.modal, {
                        transform: [
                            {
                                scale: this.state.scale
                            },
                            {
                                translateX: this.state.x
                            }
                        ]
                    }]}>

                    <View style={styles.modalContainer}>
                        <Text style={styles.title}>Llamada de emergencia</Text>
                        <Text style={styles.line}>─────────────────────────</Text>

                        <View style={{flexDirection: 'row', width: wp('70%'), paddingTop:10}}>
                            <Image 
                                source={require('../assets/icons/ambulancia.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38, paddingLeft: 40}}/>
                            <Text style={{paddingLeft: 30}}>Ambulancia</Text>
                            <View style={{paddingLeft: wp('17%')}}>
                                <Image 
                                    source={require('../assets/icons/llamada.png')}
                                    resizeMode='contain' 
                                    style={{width:30, height:30}}/>
                            </View>
                        </View>

                        
                        <View style={{flexDirection: 'row', width: wp('70%'), paddingTop:10}}>
                            <Image 
                                source={require('../assets/icons/camion-de-bomberos.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38, paddingLeft: 40}}/>
                            <Text style={{paddingLeft: 30}}>Bomberos</Text>
                            <View style={{paddingLeft: wp('21%')}}>
                                <Image 
                                    source={require('../assets/icons/llamada.png')}
                                    resizeMode='contain' 
                                    style={{width:30, height:30}}/>
                            </View>
                        </View>

                        
                        <View style={{flexDirection: 'row', width: wp('70%'), paddingTop:10}}>
                            <Image 
                                source={require('../assets/icons/divisa.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38, paddingLeft: 40}}/>
                            <Text style={{paddingLeft: 30}}>Policia</Text>
                            <View style={{paddingLeft: wp('28%')}}>
                                <Image 
                                    source={require('../assets/icons/llamada.png')}
                                    resizeMode='contain' 
                                    style={{width:30, height:30}}/>
                            </View>
                        </View>

                        
                        <View style={{flexDirection: 'row', width: wp('70%'), paddingTop:10}}>
                            <Image 
                                source={require('../assets/icons/seguridad.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38, paddingLeft: 40}}/>
                            <Text style={{paddingLeft: 30}}>Seguros mundial</Text>
                            <View style={{paddingLeft: wp('8%')}}>
                                <Image 
                                    source={require('../assets/icons/llamada.png')}
                                    resizeMode='contain' 
                                    style={{width:30, height:30}}/>
                            </View>
                        </View>


                        <View style={{flexDirection: 'row', width: wp('70%'), paddingTop:10}}>
                            <Image 
                                source={require('../assets/icons/auriculares.png')}
                                resizeMode='contain' 
                                style={{width:30, height:30, opacity:0.38, paddingLeft: 40}}/>
                            <Text style={{paddingLeft: 30}}>Asesor quality</Text>
                            <View style={{paddingLeft: wp('13%')}}>
                                <Image 
                                    source={require('../assets/icons/llamada.png')}
                                    resizeMode='contain' 
                                    style={{width:30, height:30}}/>
                            </View>
                        </View>

                        <Button onPress={this.hideModal} transparent style={styles.button}><Text style={{color:'black'}}>CANCELAR</Text></Button>
                    </View>
                </Animated.Modal>
            </View>

        <Header style={styles.container}>
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
            <MenuItem onPress={this.getProfile}>Perfil</MenuItem>
            <MenuItem onPress={() => Actions.logIn()}>Cerrar sesión</MenuItem>
          </Menu>   
          </Right>    
        </Header>
        <Content>
          <View style={{paddingTop:10, paddingLeft:5}}>
              <Card style={{width: wp('96%')}}>
                  <CardItem cardBody>
                    <Image source={require('../assets/images/imagen.png')} style={{height:  hp('35%'), width:  wp('95%'), flex: 1}}/>
                  </CardItem>
                  <CardItem style={{ width:wp('90%'), position:'relative', left:10}}>
                    <Button transparent onPress={this.request}>
                      <Text style={{color:'rgba(0,0,0,0.4)'}}>
                        ¿Aún no tienes tu SOAT asociado?{"\n"}
                      <Text style={{fontWeight: "bold"}}>Solicitalo acá</Text>
                      </Text>
                    </Button>
                  </CardItem>
              </Card>
          </View>
        </Content>
        <Footer style={styles.color_footer}>
          <FooterTab style={styles.color_footer}>
            <Button onPress={this.scaleModal}>
            <Image source={require('../assets/icons/call.png')} style={{height:  30, width:  30, flex: 1, opacity:0.38}}/>
            </Button>
            <Button  onPress={this.requestPolicy}>
            <Image source={require('../assets/icons/compra.png')} style={{height:  30, width:  30, flex: 1, opacity:0.38}}/>
            </Button>
            <Button>
            <Image source={require('../assets/icons/historial.png')} style={{height:  30, width:  30, flex: 1, opacity:0.38}}/>
            </Button>

          </FooterTab>
      </Footer>
      </Container>

    );
  }
}


const styles = StyleSheet.create({
    container1: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#05071e'
    },
    modal: {
        position: 'absolute',
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.4)'
    },
    modalContainer: {
        height: hp('50%'),
        width: wp('80%'),
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'white'
    },
    button: {
        position: 'absolute',
        top: hp('43%'),
        left: wp('51%'),
    },
    title: {
        position: 'absolute',
        top: hp('3%'),
        left: wp('7%'),
        fontSize: 20
    },
    line: {
        color: 'rgba(0,0,0,0.1)',
        position: 'absolute',
        top: hp('8%'),
    },
    container: {
        backgroundColor: '#05071e',
        paddingTop:5,
        paddingTop:20
    },
    color_footer: {
      backgroundColor: '#e9ebe2',
    },

});