import { logout } from '../../api/authentication/authAPI';
import { Redirect } from 'react-router';

const Logout = (props) => {

    const handleLogout = async () => {
        try {
            logout().then((response) => { localStorage.removeItem('access_token'); localStorage.removeItem('refresh_token')})
        } catch (e) {
            console.log(e)
        }
    }

    if (localStorage.getItem('access_token') === null) {
        return(
            <div>
                <h2> Something went wrong!!! Maybe you are not logged in!!! </h2>
            </div>
        )
    } else {
        handleLogout()
        props.setIsAuth(false)
        return <Redirect to = "/login"/>
    }
}

export default Logout;