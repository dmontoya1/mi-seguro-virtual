import React, { Component } from 'react';
import { Container, Header, Content, Button, Icon, Text, View,  Form, Item, Input, Label  } from 'native-base';
import {StyleSheet, Image} from 'react-native';

import { Actions } from 'react-native-router-flux';

import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
} from 'react-native-responsive-screen';

export default class Splash extends Component {


  render() {
    return (
      <Container style={styles.container}>
        <Content>
        <Button transparent onPress={() => Actions.intro()} style={{width:350, height:350,position: 'relative', top:hp('15%')}} >
          <Image 
              source={require('../assets/images/LogoO.png')}
              resizeMode='contain'
              style={{width:350, height:350}}/>
        </Button>
        </Content>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
    container: {
      backgroundColor: '#192a56',
      paddingTop:20
    },
    title: {
      color: 'white',
      fontSize: 39,
      fontFamily: 'Pacifico-Regular',
      textAlign: 'center',
      paddingTop: 60,
      paddingBottom: 50,
    },
    button: {
      borderRadius: 10,
    },
    button2: {
      borderRadius: 10,
      borderWidth: 1,
      borderColor: '#fff'
    },
    textInput: {
      color: 'rgba(255,255,255,.6)',
     },
  });