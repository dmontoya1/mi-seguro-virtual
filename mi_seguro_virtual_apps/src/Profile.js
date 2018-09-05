import React, { Component } from 'react';
import { Container, Header, Left, Body, Right, Button, Icon, Title, Input, Item, Label, View } from 'native-base';
import { Image, StyleSheet } from 'react-native';

import { Actions } from 'react-native-router-flux';

export default class Profile extends Component {
  render() {
    return (
      <Container style={{paddingTop:20}}>
        <Header style={styles.container}>
          <Left>
            <Button transparent onPress={() => Actions.pop()}>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body style={{paddingRight:80}}>
            <Title>Perfil</Title>
          </Body>
        </Header>
        <View style={styles.container_form}>
          <View style={{flexDirection: 'row', paddingLeft:-5, paddingTop:40, paddingRight:40}}>
              <View style={{paddingLeft:-5, paddingTop:10}}>
                <Image source={require('../assets/icons/name.png')} resizeMode='contain' style={{width:40, height:40, opacity:0.38}} />
              </View>
              <View style={{paddingLeft:10}}>
                <Item stackedLabel style={styles.input}>
                    <Label style={{color:'rgba(0,0,0,0.4)', paddingLeft:5}}>Nombre</Label>
                    <Input  disabled={true} style={{width:250}} defaultValue='Jorge' />
                </Item>
              </View>
          </View>
          <View style={{paddingLeft:50, paddingTop:20}}>
            <Item stackedLabel style={styles.input}>
                <Label style={{color:'rgba(0,0,0,0.4)', paddingLeft:5}}>Apellidos</Label>
                <Input  disabled={true} style={{width:250}} defaultValue='Salazar' />
            </Item>
          </View>
          <View style={styles.container_input}>
          <View style={{paddingLeft:-5, paddingTop:10}}>
            <Image source={require('../assets/icons/cellphone.png')} resizeMode='contain' style={{width:40, height:40, opacity:0.38}} />
          </View>
            <View style={{paddingLeft:10}}>  
              <Item stackedLabel style={styles.input}>
              <Label style={{color:'rgba(0,0,0,0.4)', paddingLeft:5}}>Celular de contacto</Label>
                  <Input  disabled={true} style={{width:250}} defaultValue='(+57) 320 320 5868' />
              </Item>
            </View>
          </View>
          <View style={styles.container_input}>
            <View style={{paddingLeft:-5, paddingTop:10}}>
              <Image source={require('../assets/icons/mail.png')} resizeMode='contain' style={{width:40, height:40, opacity:0.38}} />
            </View>
            <View style={{paddingLeft:10}}>  
              <Item stackedLabel style={styles.input} >
                  <Label style={{color:'rgba(0,0,0,0.4)', paddingLeft:5}}>Correo electrónico</Label>
                  <Input  disabled={true} style={{width:250}} defaultValue='correo@correo.com.co' />
              </Item>
            </View>
          </View>
        </View>
        <View style={{paddingLeft:270, paddingTop: 100}}>
          <Button transparent style={{width:65, height:65}}>
            <Image 
              source={require('../assets/icons/edit.png')} 
              resizeMode='contain' 
              style={{width:60, height:60}} />
          </Button>
        </View>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#05071e',
  },
  input: {
    backgroundColor: 'rgb(250,250,250)',
    borderBottomColor: '#05071e',
    paddingLeft: 20,
  },
  container_form: {
      paddingLeft: 20,
      paddingRight: 20,
  },
  container_input: {
    flexDirection: 'row',
    paddingLeft:-5,
    paddingTop:20,
    paddingRight:40
  },
});