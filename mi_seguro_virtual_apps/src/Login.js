import React, { Component } from 'react';
import { Container, Header, Content, Button, Icon, Text, View,  Form, Item, Input, Label  } from 'native-base';
import {StyleSheet} from 'react-native';

export default class ButtonIconExample extends Component {
  render() {
    return (
      <Container style={styles.container}>
        <Content>
        <Text style={styles.title}>MI Seguro Virtual</Text>
        <View style={styles.button}>
            <Button iconLeft>
                <Icon name='home'/>
                <Text>Home</Text>
            </Button>
            <Button iconLeft>
                <Icon name='home' />
                <Text>Home</Text>
            </Button>
        </View>
        <Form>
            <Item inlineLabel>
              <Label style={styles.text}>Correo electronico</Label>
              <Input />
            </Item>
            <Item inlineLabel last>
              <Label style={styles.text}>Contraseña</Label>
              <Input />
            </Item>
        </Form>
        <Button full danger style={{paddingTop: 30}}>
            <Text>INICIAR SESIÓN</Text>
        </Button>
        <Button full transparent dark style={styles.button2}>
            <Text>REGISTRARSE</Text>
        </Button>
        </Content>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
    container: {
      backgroundColor: '#192a56',
    },
    title: {
      color: 'white',
      fontSize: 40,
      textAlign: 'center',
      paddingTop: 60,
      paddingBottom: 50,
    },
    button: {
        flexDirection:'row',
        paddingBottom: 30,
        paddingLeft: 80,
    },
    button2: {
        color : 'white',
        paddingTop: 20,
        borderColor: 'white',
    },
  });