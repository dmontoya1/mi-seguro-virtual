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
    Animated
} from 'react-native';

import Modal from 'react-native-root-modal';

import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

import { Actions } from 'react-native-router-flux';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';




export default class Insurance extends Component {

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
            <Text style={{color:'white'}}>Seguros comprados</Text>
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
            <MenuItem onPress={() => Actions.profile()}>Perfil</MenuItem>
            <MenuItem onPress={() => Actions.logIn()}>Cerrar sesión</MenuItem>
          </Menu>   
          </Right>    
        </Header>
        <View style={{position:'relative', top:30,left: wp('15%')}}>
          <Image 
            source={require('../assets/images/imagen.png')}
            style={{width:250, height:300}}
          />
        </View>
        <View style={{paddingTop:10}}>
          <Text style={styles.line}>───────────────────────────────</Text>
        <View>
          <Text>Placa</Text>
          <Text>###-###</Text>
        </View>
        </View>

        
      </Container>

    );
  }
}


const styles = StyleSheet.create({
    container: {
        backgroundColor: '#05071e',
        paddingTop:5
    },
    color_footer: {
      backgroundColor: '#e9ebe2',
    },
    line: {
        color: 'rgba(0,0,0,0.4)',
        position: 'absolute',
        top: hp('8%'),
    },

});