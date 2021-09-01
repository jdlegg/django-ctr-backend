import { useState } from "react";
import { loginUser } from '../../api/authentication/authAPI';
import { Redirect } from 'react-router';

const Login = (props) => {

    const [username, setUsername] = useState('') // username to create credentials
    const [password, setPassword] = useState('') // password to create credentials
    const [redirect, setRedirect] = useState(false) // handler to redirect if authenticated
    const [errorMessage, setErrorMessage] = useState('') // handler for error message
    
    // store credentials into state
    const handleChange = (e) => {
        if (e.target.name === 'username') {
            setUsername(e.target.value)
        } else if (e.target.name === 'password') {
            setPassword(e.target.value)
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault(); // stop default actions from happening on submit
        // build user cred object to pass to authAPI components
        const userCred = {
            username: username,
            password: password,
        }
        //console.log(userCred)
        // pass userCreds into loginUser
        loginUser(userCred)
            .then( async (response) => { 
                // Create error message
                if (response.status !== 200) {
                    let error = await response.json()
                    setErrorMessage(error.detail)
                } else {
                    // Set localStorage with tokens and isAuth/Redirect
                    let token = await response.json()
                    console.log("Token: ",token);
                    localStorage.setItem('access_token', token.access);
                    localStorage.setItem('refresh_token', token.refresh);
                    props.setIsAuth(true);
                    setRedirect(true);
                }})
    }

    if (redirect) {
        return <Redirect to = "/protected"/> // move here if redirected
    }

    return(
        <div>Login
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input name="username" type="text" value={username} onChange={handleChange}/>
                </label>
                <label>
                    Password:
                    <input name="password" type="password" value={password} onChange={handleChange}/>
                </label>
                <input type="submit" value="Submit"/>
                { errorMessage && <h3 className="error"> {errorMessage} </h3>}
            </form>
        </div>
    )
}

export default Login;