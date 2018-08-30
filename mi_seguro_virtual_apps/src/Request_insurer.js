import React, { Component } from 'react';
import { Accordion, Content, Container, Header, Left, Body, Right, Button, Icon, Card, CardItem, View, Text } from 'native-base';
import { Image, StyleSheet,TouchableOpacity } from 'react-native';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';


import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

export default class Request extends Component {
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
  render() {
    return (
      <Container>
        <Header style={styles.container}>
          <Left>
            <Button transparent>
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
            <MenuItem onPress={this.hideMenu}>Perfil</MenuItem>
            <MenuItem onPress={this.hideMenu}>Cerrar sesión</MenuItem>
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
                            <Image 
                                source={require('../assets/icons/camara.png')}
                                style={{width:40, height:40}}
                            />
                        </View>
                    </View>
                    <View style={{flexDirection: 'row', paddingTop:20}}>
                        <View>
                            <Text style={{color:'rgba(0,0,0,1)', fontSize:13, position:'relative', top:-5, right:10}}>
                                Fotografía de tu licencua de conducción.
                            </Text>
                        </View>
                        <View style={{position:'relative', top:-15, left:wp('5%')}}>
                            <Image 
                                    source={require('../assets/icons/camara.png')}
                                    style={{width:40, height:40}}
                                />
                        </View>
                    </View>
                  </View>
                </CardItem>
            </Card>
        </View>
      </Container>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    backgroundColor: '#05071e',
  },
});