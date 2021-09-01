import { useState, useEffect } from "react";
import{ prot } from '../api/authentication/authAPI';
import { Redirect } from 'react-router';

const Prote = (props) => {

    const [prote, setProte] = useState();

    useEffect( () => {
        prot().then((response) => {
            if(response === false) {
            //console.log("Inside Prote false");
            //console.log("isAuth: ", props.isAuth)
            props.setIsAuth(false);
            //console.log("After set - isAuth: ", props.isAuth)
            return <Redirect to = "/login/"/>
        } else { setProte(response)} })
    }, [])
    

    return(
        <div>Protected
            <p>
                Output:
            </p>
            {prote}
        </div>
    )
}

export default Prote;