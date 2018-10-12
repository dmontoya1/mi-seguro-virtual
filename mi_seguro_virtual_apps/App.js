
import React, {Component} from 'react';
import {AsyncStorage, ActivityIndicator} from 'react-native';

import { Router, Scene, Stack } from 'react-native-router-flux';

import Splash from './src/Splash';
import Login from './src/Login';
import SignUp from './src/Sign_up';
import Profile from './src/Profile';
import ProfileEdit from './src/Profile_edit';
import Dashboard from './src/Dashboard';
import Request from './src/Request_insurer';
import IntroView from './src/pageView/IntroView';
import Insurance from './src/Insure_Bought';

import deviceStorage from './src/deviceStorage';

export default class App extends Component {

  constructor() {
    super();
    this.state = {
      jwt: '',
      stepper: false,
      loading: true
    }

    this.newJWT = this.newJWT.bind(this);
    this.stepperComplete = this.stepperComplete.bind(this);
    this.deleteJWT = deviceStorage.deleteJWT.bind(this);
    this.loadJWT = deviceStorage.loadJWT.bind(this);
    this.loadStepper = deviceStorage.loadStepper.bind(this);
    this.loadJWT();
    this.loadStepper();
  }

  newJWT(jwt){
    state = {};
    this.setState({
      jwt: jwt
    });
  }

  stepperComplete(){
    this.setState({
      stepper: true
    });
  }

  render() {
    if (this.state.loading) {
      return (
        <ActivityIndicator />
      );
    }
    else{
      return (
        <Router>
          <Stack key="root">
            <Scene 
              key="intro" 
              component={IntroView} 
              hideNavBar={true}
              stepperComplete={this.stepperComplete}
              initial={!this.state.stepper && !this.state.jwt}
            />
            <Scene 
              key="logIn"
              component={Login}
              hideNavBar={true}
              newJWT={this.newJWT}
              initial={this.state.stepper && !this.state.jwt}
            />
            <Scene key="signUp" component={SignUp} hideNavBar={true}/>
            <Scene 
              key="home" 
              component={Dashboard} 
              hideNavBar={true}
              initial={this.state.stepper && this.state.jwt}
            />
            <Scene key="insurance" component={Insurance} hideNavBar={true}/>
            <Scene key="request" component={Request} hideNavBar={true}/>
            <Scene key="profile" component={Profile} hideNavBar={true}/>
            <Scene key="profile_edit" component={ProfileEdit} hideNavBar={true}/>
          </Stack>
        </Router>
      );
    }
  }

}

