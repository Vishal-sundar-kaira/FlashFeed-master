import React from 'react';
import { View, Text, Image, TouchableOpacity,Linking } from 'react-native';

const NewsItem = (props) => {
  const { title, description, imageurl, newsurl, author, date } = props;

  return (
    <View style={{ marginVertical: 10, borderRadius: 8, overflow: 'hidden',width: '100%',alignItems:"center",justifyContent:"center"}}>
      <Image
        source={{ uri: imageurl ? imageurl : 'https://images.hindustantimes.com/tech/img/2022/12/17/1600x900/firmbee-com-eMemmpUojlw-unsplash_1648476869035_1671275624857_1671275624857.jpg' }}
        style={{ height: 200, resizeMode: 'cover',width: '100%' }}
      />
      <View style={{ padding: 15,width:'100%'}}>
        <Text style={{ fontSize: 18, fontWeight: 'bold', marginBottom: 8 }}>{title}...</Text>
        <Text style={{ fontSize: 14, marginBottom: 8 }}>{description}...</Text>
        <Text style={{ fontSize: 12, color: 'gray', marginBottom: 8 }}>
           Author: {!author ? 'unknown' : author} Last updated on {new Date(date).toGMTString()}
        </Text>
        <TouchableOpacity
          onPress={() => Linking.openURL(newsurl)}
          style={{ backgroundColor: '#6C44E9', padding: 10, borderRadius: 5, alignItems: 'center' }}
        >
          <Text style={{ color: 'white' }}>Read More</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default NewsItem;
