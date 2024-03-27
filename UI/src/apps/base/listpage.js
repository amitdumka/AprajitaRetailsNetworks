


function ListPage(props) {
    return (
        <div>
            <h1>Base List Page</h1>
        </div>
    );
}

ListPage.propTypes = {
    title: PropTypes.string.isRequired,
    route: PropTypes.string,
    apiurl: PropTypes.string, 
    baseurl: PropTypes.string.isRequired,
    className: PropTypes.string.isRequired,
    
}

export default ListPage