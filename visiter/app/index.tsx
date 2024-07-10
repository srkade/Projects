import { Link } from 'expo-router';
import React from 'react';
import {Text, View } from 'react-native';


export default function App() {
  return (
    <View className="flex-1 items-center justify-center bg-white">
    <Text>Open up App.js to start working on your app!</Text>
    <Link href="">create pass</Link>
    
  </View>
  );
}

 const styles = StyleSheet.create({
   container: {
     flex: 1,
     backgroundColor: '#fff',
     alignItems: 'center',
     justifyContent: 'center',
   },
 });