import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Clients.styles';

class Clients extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Clients will mount');
  }

  componentDidMount = () => {
    console.log('Clients mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Clients will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Clients will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Clients did update');
  }

  componentWillUnmount = () => {
    console.log('Clients will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="ClientsWrapper">
        Test content
      </div>
    );
  }
}

Clients.propTypes = {
  // bla: PropTypes.string,
};

Clients.defaultProps = {
  // bla: 'test',
};

const mapStateToProps = state => ({
  // blabla: state.blabla,
});

const mapDispatchToProps = dispatch => ({
  // fnBlaBla: () => dispatch(action.name()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Clients);
