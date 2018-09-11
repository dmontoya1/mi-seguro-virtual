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


import Menu, { MenuItem, MenuDivider } from 'react-native-material-menu';

import { Actions } from 'react-native-router-flux';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';

import Swiper from 'react-native-swiper';




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
        let token = this.props.token;
        let policy = this.props.policy[0];
        return (

        <Container style={{paddingTop:20}}>
        <Header style={styles.container}>
          <Left>
            <Button transparent onPress={() => Actions.pop({token:token})}>
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
            <MenuItem onPress={() => {}}>Perfil</MenuItem>
            <MenuItem onPress={() => Actions.logIn()}>Cerrar sesión</MenuItem>
          </Menu>   
          </Right>    
        </Header>
        <View>
          <Image
            source={require('../assets/images/imagen.png')}
            style={{position:'relative', left:wp('17.5%'), top:40,  width:wp('65%'), height:hp('50%')}} 
          />
          <View style={{position:'relative', top: 50 }}>
            <Text style={{color: 'rgba(0,0,0,0.3)', paddingTop:30}}>───────────────────────────────</Text>
            <View style={styles.textContainer}>
              <View>
                <Text style={{opacity:0.38}}>Aseguradora</Text>
              </View>
              <View style={{paddingLeft: wp('42%')}}>
                <Text>{policy.insurer}</Text>
              </View>
            </View>

            <View style={styles.textContainer}>
              <View>
                <Text style={{opacity:0.38}}>Seguro</Text>
              </View>
              <View style={{paddingLeft: wp('54%')}}>
                <Text>{policy.insurance}</Text>
              </View>
            </View>

            <View style={styles.textContainer}>
              <View>
                <Text style={{opacity:0.38}}>Fecha vencimiento</Text>
              </View>
              <View style={{paddingLeft: wp('30%')}}>
                <Text>{policy.expiration_date}</Text>
              </View>
            </View>
          </View>
        </View>
      </Container>

    );
  }
}


const styles = StyleSheet.create({
    container: {
        backgroundColor: '#05071e'
    },
    color_footer: {
      backgroundColor: '#e9ebe2',
    },
    line: {
        color: 'rgba(0,0,0,0.4)',
        position: 'absolute',
        top: hp('8%'),
    },
    imageContainer: {
      flex:2,
      alignSelf: 'stretch',
      alignItems: 'center',
      justifyContent: 'center',
    },
    textContainer: {
      width: wp('80%'),
      flexDirection: 'row',
      paddingHorizontal: 20,
      paddingTop:15
    },
    dotStyle: {
      backgroundColor: 'rgba(0,0,0,.3)', 
      width: 10, 
      height: 10, 
      borderRadius: 7, 
      marginLeft: 7, 
      marginRight: 7
    },
  
    dotActivateStyle: {
      backgroundColor: '#000', 
      width: 10, 
      height: 10, 
      borderRadius: 7, 
      marginLeft: 7, 
      marginRight: 7
    },

});