
import React, {Component} from 'react';
import {AsyncStorage} from 'react-native';

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

export default class App extends Component {
  
  render() {
    return (
      <Router>
      <Stack key="root">
        <Scene key="intro" component={IntroView} hideNavBar={true}/>
        <Scene key="logIn" component={Login} hideNavBar={true}/>
        <Scene key="signUp" component={SignUp} hideNavBar={true}/>
        <Scene key="home" component={Dashboard} hideNavBar={true}/>
        <Scene key="insurance" component={Insurance} hideNavBar={true}/>
        <Scene key="request" component={Request} hideNavBar={true}/>
      </Stack>
    </Router>
    );
  }
}


