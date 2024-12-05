import { apiClient } from '@app/clients/axios';
import { log } from '@app/utils/logs';
import { useNavigation } from '@react-navigation/native';
import React, { useState, useEffect, useRef } from 'react';
import { Image, View, TouchableOpacity, Linking } from 'react-native';
import { Text, TextInput } from 'react-native-paper';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '@app/store';
import { setOtpCode } from '@app/store/slices/app';
import { styles } from '@app/styles/auth';
import { Screen } from '@app/components/Screen';

export const SignupVerify = () => {
  const navigation = useNavigation<any>();
  const dispatch = useDispatch();
  const state = useSelector((state: RootState) => state.app);
  const firstRender = useRef(true);
  const [otp, setOtp] = useState('');
  const [message, setMessage] = useState<any>('');
  const [disabled, setDisabled] = useState(true);

  const handleSubmit = () => {
    apiClient
      .get(`/signup-verify/${otp}`)
      .then(response => {
        if (response.status === 200) {
          setDisabled(true);
          dispatch(setOtpCode(''));
          log('Account activated ' + response.data);
          goToSignin();
        }
      })
      .catch((error: any) => {
        if (error.response) {
          setMessage(Object.values(error.response.data.message));
        } else {
          setMessage('Verification not successful this time!');
          log('Verification not successful: ' + error);
        }
      });
  };

  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    setDisabled(validateForm);
  }, [otp]);

  const validateForm = () => {
    if (!/^(?!\s*$).+/.test(otp)) {
      setMessage(' Invalid otp ');
      return true;
    } else {
      setMessage('');
      return false;
    }
  };

  const goHome = () => {
    navigation.navigate('Home');
  };

  const goToSignin = () => {
    navigation.navigate('SigninScreen');
  };

  const goToMobileSignupVerifyResend = () => {
    navigation.navigate('MobileSignupVerifyResendScreen');
  };

  const goToEmailSignupVerifyResend = () => {
    navigation.navigate('EmailSignupVerifyResendScreen');
  };

  return (
    <Screen>
      <View style={styles.container}>
        <Image
          source={require('../../assets/images/logo.png')}
          style={styles.imageStyle}
        />
        <View style={styles.headerContainer}>
          <Text style={styles.headerText}>EasyFinance</Text>
        </View>
        <Text style={styles.subHeaderText}>SIGN UP VERIFICATION</Text>
        <View style={styles.sectionContainer}>
          <Text> </Text>
        </View>
        <View style={styles.switchContainer}>
          <Text style={styles.errorText}>{message}</Text>
          <Text>Your OTP is: {state.otpCode}</Text>
        </View>
        <View style={styles.sectionContainer}>
          <TextInput
            value={otp}
            label={'One time password(OTP)'}
            mode='outlined'
            autoCapitalize="none"
            autoCorrect={false}
            autoFocus={true}
            style={styles.input}
            onChangeText={otp => setOtp(otp)}
          />
        </View>
        <TouchableOpacity
          style={styles.button}
          disabled={disabled}
          onPress={() => handleSubmit()}>
          <Text style={styles.buttonText}>Verify</Text>
        </TouchableOpacity>
        <View style={styles.switchContainer}>
          <TouchableOpacity onPress={() => goHome()}>
            <Text style={styles.switchAction}>Cancel</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.switchContainer}>
          <TouchableOpacity onPress={() => goToMobileSignupVerifyResend()}>
            <Text style={styles.switchAction}>Resend Code - Mobile</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.switchContainer}>
          <TouchableOpacity onPress={() => goToEmailSignupVerifyResend()}>
            <Text style={styles.switchAction}>Resend Code - Email</Text>
          </TouchableOpacity>
        </View>
        <Text
          onPress={() => {
            Linking.openURL('http://easyfinance.org');
          }}>
          Visit http://easyfinance.org
        </Text>
      </View>
    </Screen>
  );
};
