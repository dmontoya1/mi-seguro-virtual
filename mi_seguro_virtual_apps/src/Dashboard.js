import React, { Component } from 'react';
import { Accordion, Content,Footer, FooterTab, Container, Header, Left, Body, Right, Button, Icon, Card, CardItem, View, Text } from 'native-base';
import { Image, StyleSheet,TouchableOpacity } from 'react-native';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';


import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

export default class Dashboard extends Component {
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
        <Content>
          <View style={{paddingTop:10, paddingLeft:5}}>
              <Card style={{width: wp('96%')}}>
                  <CardItem cardBody>
                    <Image source={require('../assets/images/imagen.png')} style={{height:  hp('35%'), width:  wp('95%'), flex: 1}}/>
                  </CardItem>
                  <CardItem style={{ width:wp('90%'), position:'relative', left:10}}>
                    <Button transparent>
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
            <Button>
            <Image source={require('../assets/icons/call.png')} style={{height:  30, width:  30, flex: 1, opacity:0.38}}/>
            </Button>
            <Button>
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
  container: {
    backgroundColor: '#05071e',
  },
  color_footer: {
      backgroundColor: '#e9ebe2',
  },
});