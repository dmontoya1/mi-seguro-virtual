import React, { Component } from 'react';
import { Container, Header, Left, Body, Right, Button, Icon, Card, CardItem, View, Text } from 'native-base';
import { Image, StyleSheet } from 'react-native';
import {
  widthPercentageToDP as wp,
  heightPercentageToDP as hp,
  listenOrientationChange as loc,
  removeOrientationListener as rol
} from 'react-native-responsive-screen';

export default class Dashboard extends Component {

  constructor() {
        super();
    
        //this.state = false;

        setState = () =>{
          this.state = !this.state;   
        }
  }

  componentDidMount() {
    //this.setState();
    loc(this);
  }
  
  componentWillUnMount() {
    //this.setState();
    rol();
  }
  render() {
      //let style = {};

      /*if (this.state)s{
         style = {
              box : {
                position: 'absolute',
                top:5,
                left:wp('10%')
              }
        };
      }
      else{
           style = {
              box : {
                position: 'absolute',
                top:5,
                left:wp('50%')
              }
        };
      }*/
    return (
      <Container>
        <Header style={styles.container}>
          <Left>
            <Button transparent>
              <Icon name='arrow-back' />
            </Button>
          </Left>
          <Body >
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
        <View style={{paddingTop:10, paddingLeft:5}}>
            <Card style={{width: wp('96%')}}>
                <CardItem cardBody>
                <Image source={require('../assets/images/imagen.png')} style={{height:  hp('35%'), width:  wp('95%'), flex: 1}}/>
                </CardItem>
                <CardItem>
                    <Text style={{color:'rgba(0,0,0,0.4)'}}>
                        ¿Aun no tienes tu SOAT asociado?{"\n"}
                        <Text style={{fontWeight: "bold"}}>Solicitalo acá</Text>
                    </Text>
                      <Right>
                          <Button transparent style={{width:20, height:15, justifyContent: "center"}}>
                              <Image source={require('../assets/icons/desplegable.png')} style={{height: 50, width: 50, opacity:0.38 }}/>
                          </Button>
                      </Right>   
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
  textWrapper: {
    height: hp('70%'), // 70% of height device screen
    width: null,  // 80% of width device screen
    flex: 1
  },
});