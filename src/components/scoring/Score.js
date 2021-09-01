import { useState, useEffect } from "react";
import { Redirect } from 'react-router';
import { multi_score } from "../../api/scoring/scoringAPI";
import { useParams } from "react-router";
import { prot } from "../../api/authentication/authAPI";

const Score = (props) => {
    console.log("Score Component")
    const { name } = useParams();

    const [prote, setProte] = useState([]);

    useEffect( () => {
        multi_score(name).then((response) => {
        if(response===false) {
            props.setIsAuth(false);
            return <Redirect to = "/login/"/>
        } else {setProte(response)}
    }, [name])})

    return(
        <div>Scoring
            <p>
                Output:
            </p>
            {prote}
        </div>
    )
}

export default Score;