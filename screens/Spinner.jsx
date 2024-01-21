import React from 'react';
import { View, Image } from 'react-native';
// import spin from './spinner.gif';

const Spinner = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Image source={require('./spinner.gif')} style={{ width: 50, height: 50 }} />
    </View>
  );
};

export default Spinner;
