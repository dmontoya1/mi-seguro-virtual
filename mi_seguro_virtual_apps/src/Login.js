import React, { Component } from 'react';
import { Container, Header, Content, Button, Icon, Text, View,  Form, Item, Input, Label  } from 'native-base';
import {StyleSheet, Alert} from 'react-native';

import { Actions } from 'react-native-router-flux';

import logInPostAPI from '././api/log_in.api';

export default class Login extends Component {
  constructor(props) {
        super(props);
        this.state = {
            token: '',  
            username:'',
            password:'',
        };

        this.submit = this.submit.bind(this);
    }

    submit (){
      let {
          username,
          password,
      } = this.state;

      let dataToSend = {
            username,
            password
        };
      logInPostAPI(dataToSend).then(data => {
        if (data.errored){
          Alert.alert(
            'Error',
            "Contraseña o correo electronico incorrectos.",
            [
              {text: 'Aceptar', onPress: () =>{}},
            ],
            { cancelable: false }
          ) 
        } else {
          let token = data.data._55.token;
          Actions.home({token: token});
        }

      });
    }
  render() {
    return (
      <Container style={styles.container}>
        <Content>
        <Text style={styles.title}>mi SEGURO Virtual</Text>
        <View style={{paddingLeft:10,paddingRight:30, alignContent: 'center'}}>
          <Form style={{paddingBottom:40}}>
              <Item fixedLabel >
                <Input 
                  placeholder="Correo electrónico" 
                  placeholderTextColor='rgba(255,255,255,.6)'
                  style={styles.textInput} 
                  borderColor='rgba(255,255,255,.6)'
                  onChangeText={(username) => this.setState({username})} />
              </Item>
              <Item fixedLabel>
                <Input 
                  placeholder="Contraseña" 
                  placeholderTextColor='rgba(255,255,255,.6)' 
                  style={styles.textInput} 
                  borderColor='rgba(255,255,255,.6)' 
                  secureTextEntry={true} 
                  onChangeText={(password) => this.setState({password})} />
              </Item>
          </Form>
        </View>
        <View style={{paddingLeft:22,paddingRight:25, paddingBottom:20}}>
          <Button block danger style={styles.button} onPress={this.submit}>
              <Text>INICIAR SESIÓN</Text>
          </Button>
        </View>
        <View style={{paddingLeft:22,paddingRight:25, paddingTop:10}}>
          <Button block transparent style={styles.button2} onPress={() => Actions.signUp() }>
              <Text style={{color:'white'}}>REGISTRARSE</Text>
          </Button>
        </View>
        </Content>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
    container: {
      backgroundColor: '#192a56'
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
