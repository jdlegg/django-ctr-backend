import { getAccessToken, getRefreshToken, isTokenExpired } from "./authHelper";
import { Redirect } from 'react-router';

export const createUser = async (newUser) => {
  const response = await fetch('http://127.0.0.1:8000/api/user/create/', {
  //const response = await fetch('https://young-shore-38212.herokuapp.com/api/user/create/', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(newUser)
  })
  return response
};

export const loginUser = async (userCred) => {
    const response = await fetch('http://127.0.0.1:8000/api/token/obtain/', {
    //const response = await fetch('https://young-shore-38212.herokuapp.com/api/token/obtain/', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'POST',
    body: JSON.stringify(userCred)
    })
    return response
}

export const logout = async () => {
    let dataAccess = getAccessToken();
    let dataRefresh = getRefreshToken();

    if (dataAccess === false || dataRefresh === false) {
        return false;
    }

    console.log(dataRefresh)
    const response = await fetch('http://127.0.0.1:8000/api/blacklist/', {
    //const response = await fetch('https://young-shore-38212.herokuapp.com/api/blacklist/', {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': "JWT " + dataAccess,
    },
    method: 'POST',
    body: JSON.stringify({refresh: dataRefresh})

  })
  return response
};

export const refreshToken = async () => {
    console.log("RefreshToken")
    let dataAccess = getAccessToken();
    let dataRefresh = getRefreshToken();

    if (dataAccess === false || dataRefresh === false) {
        return false;
    }

    const response = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
    //const response = await fetch('https://young-shore-38212.herokuapp.com/api/token/refresh/', {  
    headers: {
      'Content-Type': 'application/json',
      'Authorization': "JWT " + dataAccess,
    },
    method: 'POST',
    body: JSON.stringify({refresh: dataRefresh})
  })

  if (response.status === 200) {
    const token = await response.json()
    localStorage.setItem('access_token', token.access)
    localStorage.setItem('refresh_token', token.refresh)
  }
  return response.data
};

export const prot = async () => {
    let dataAccess = getAccessToken();
    //console.log("Debug prot: ",dataAccess)
    if (dataAccess === false) {
        return false;
    } 

    if (!isTokenExpired(dataAccess)) {
        refreshToken().then((response) => {
            if(response === false) {
                return <Redirect to="/login" />
            } else {
                dataAccess = getAccessToken();
            }
        })
    }

    const response = await fetch('http://127.0.0.1:8000/api/hello/', {
    //const response = await fetch('https://young-shore-38212.herokuapp.com/api/hello/', {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': "JWT " + dataAccess,
    },
    method: 'GET'
  })
  return response.text()
};

