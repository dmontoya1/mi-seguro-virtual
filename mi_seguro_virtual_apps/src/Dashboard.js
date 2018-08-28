import React, { Component } from 'react';
import { Container, Header, Left, Body, Right, Button, Icon, Card, CardItem, View, Text } from 'native-base';
import { Image, StyleSheet } from 'react-native';

export default class Dashboard extends Component {
  render() {
    return (
      <Container>
        <Header style={styles.container}>
          <Left>
            <Button transparent>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body style={{paddingLeft:40, paddingTop:10}}>
            <Image 
                source={require('../assets/images/logo.png')}
                resizeMode='contain' 
                style={{width:150, height:30}}
            />
          </Body>
          <Right>
              <Button transparent style={{width:70, height:70}}>
                <Image 
                    source={require('../assets/icons/cuenta.png')} 
                    resizeMode='contain' 
                    style={{width:50, height:50}}
                />     
              </Button>    
          </Right>    
        </Header>
        <View style={{paddingTop:10, paddingLeft:7}}>
            <Card style={{width:340}}>
                <CardItem cardBody>
                <Image source={require('../assets/images/imagen.png')} style={{height: 200, width: null, flex: 1}}/>
                </CardItem>
                <CardItem>
                    <Text style={{color:'rgba(0,0,0,0.4)'}}>
                        ¿Aun no tienes tu SOAT asociado?{"\n"}
                        <Text style={{fontWeight: "bold"}}>Solicitalo acá</Text>
                    </Text>
                    <View style={{paddingLeft:35}}>
                        <Button transparent style={{width:20, height:15, justifyContent: "center"}}>
                            <Image source={require('../assets/icons/desplegable.png')} style={{height: 50, width: 50, opacity:0.38 }}/>
                        </Button>
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