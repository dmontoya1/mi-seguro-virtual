import React, { Component } from 'react';
import { Container, CheckBox, Header, Left, Body, Right, Button, Icon, Title,Form, Item, Input, Label, View } from 'native-base';
import {StyleSheet,ScrollView,Text,Alert} from 'react-native';

import { Actions } from 'react-native-router-flux';

import signUpPostAPI from '././api/sign_up.api';

export default class SignUp extends Component<{}> {
    constructor(props) {
        super(props);
        this.state = {
            checked: false,
            first_name:'',
            last_name:'',
            document_number:'',
            cellphone_number:'',
            mail:'',
            mail2:'',
            password:'',
            password2:''
        };

        this.submit = this.submit.bind(this);
    }

    submit() {
        let {
            first_name,
            last_name,
            document_number,
            cellphone_number,
            mail,
            mail2,
            password,
            password2  
        } = this.state;

        if (password !== password2) {
            Alert.alert(
              'Error',
              'Las contraseñas no coinciden.',
              [
                {text: 'OK', onPress: () => console.log('OK Pressed')},
              ],
              { cancelable: false }
            )
        } else if (mail2 !== mail) {
            Alert.alert(
              'Error',
              'Las direcciones de correo no coinciden.',
              [
                {text: 'OK', onPress: () => console.log('OK Pressed')},
              ],
              { cancelable: false }
            )
            return;
        }

        let dataToSend = {
            first_name,
            last_name,
            document_number,
            cellphone_number,
            email:mail,
            username:mail,
            password
        };

        signUpPostAPI(dataToSend).then(data => {
            if (data.errored) {
                console.warn(data);
            } else {
                Alert.alert(
                  'Registro exitoso',
                  "Ahora puedes solicitar tu SOAT y otros seguros a través de la aplicación y llevarlos en todo momento.",
                  [
                    {text: 'Aceptar', onPress: () => Actions.logIn()},
                  ],
                  { cancelable: false }
                )     
                }
        });
    }

    render() {
        const { checked } = this.state;
        return (
            <Container>
                <Header style={styles.header}>
                    <Left>
                        <Button transparent onPress={() => Actions.pop()}>
                            <Icon name='arrow-back' />
                        </Button>
                    </Left>
                    <Body style={{paddingRight:80}}>
                        <Title>Registro</Title>
                    </Body>
                </Header>

                <ScrollView>
                    <View style={{paddingLeft:10,paddingRight:30, alignContent: 'center', paddingTop:40}}>
                        <View style={{alignContent: 'center', paddingLeft: 20}}>
                            <Text style={{color: 'rgba(0,0,0,0.3)'}}> ────────────── ó ──────────────</Text>
                        </View> 
                        <Form>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Nombres' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(first_name) => this.setState({first_name})} />
                            </Item>
                            <Item fixedLabel style={styles.input} >
                                <Input 
                                    placeholder='Apellidos' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(last_name) => this.setState({last_name})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Numero de documento' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(document_number) => this.setState({document_number})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Celular de contacto' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(cellphone_number) => this.setState({cellphone_number})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Correo electrónico' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(mail) => this.setState({mail})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Confirme su correo electrónico' 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(mail2) => this.setState({mail2})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Contraseña' 
                                    secureTextEntry={true} 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(password) => this.setState({password})} />
                            </Item>
                            <Item fixedLabel style={styles.input}>
                                <Input 
                                    placeholder='Confirmar contraseña' 
                                    secureTextEntry={true} 
                                    placeholderTextColor='rgba(0,0,0,0.4)'
                                    onChangeText={(password2) => this.setState({password2})} />
                            </Item>
                        </Form>
                        <View style={styles.checkbox_container}>
                            <View>
                                <CheckBox 
                                    checked={checked} 
                                    color='#192a56'
                                    onPress={() => this.setState({checked: !checked})}/>
                            </View>
                            <View style={{paddingLeft:30}}>
                                <Text style={{textAlign: 'left', paddingLeft:10}}>Al continuar acepta nuestros <Text style={{fontWeight: "bold"}}> Términos y {"\n"}condiciones</Text> y <Text style={{fontWeight: "bold"}}>Politica de tratamiento de datos</Text> </Text>
                            </View>
                        </View>
                        <View style={{paddingLeft:22,paddingRight:10, paddingBottom:15}}>
                            <Button block danger style={styles.button} onPress={this.submit}>
                                <Text style={{color:'white'}}>REGISTRARSE</Text>
                            </Button>
                        </View>
                    </View>
                </ScrollView>

            </Container>
        );
    }
}

const styles = StyleSheet.create({
    header: {
        backgroundColor: '#192a56',
    },
    input: {
        paddingTop: 20,    
    },
    input_end: {
        paddingBottom: 20,    
    },
    text: {
        color: 'rgba(0,0,0,0.2)'
    },
    checkbox_container: {
        paddingTop:40,
        paddingBottom:30,
        flex: 1, 
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    button: {
        borderRadius: 10,
    },
});