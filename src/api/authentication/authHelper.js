import decode from "jwt-decode";

export const isTokenExpired = (token) => {
    try {
        const decoded = decode(token);
        //console.log("Debug: ", decoded.exp)
        //console.log("Debug: ", (Date.now() / 1000) )
        if (decoded.exp > Date.now() / 1000) {
            return true;
        } else return false;
    } catch(e) {
        return false;
    }
}

export const getAccessToken = () => {
    let data = localStorage.getItem('access_token')
    if (data === null) {
        return false
    } else {
        return data;
    }
}

export const getRefreshToken = () => {
    let data = ''
    try {
        data = localStorage.getItem('refresh_token')
    } catch (e) {
        console.log(e)
        return false
    }
    return data;
}