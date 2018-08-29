/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View} from 'react-native';

import Login from './src/Login';
import SignUp from './src/Sign_up';
import Profile from './src/Profile';
import ProfileEdit from './src/Profile_edit';
import Dashboard from './src/Dashboard';

export default class App extends Component {
  render() {
    return (
      <Dashboard />
    );
  }
}


