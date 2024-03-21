import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Stores.styles';

class Stores extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Stores will mount');
  }

  componentDidMount = () => {
    console.log('Stores mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Stores will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Stores will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Stores did update');
  }

  componentWillUnmount = () => {
    console.log('Stores will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="StoresWrapper">
        Test content
      </div>
    );
  }
}

Stores.propTypes = {
  // bla: PropTypes.string,
};

Stores.defaultProps = {
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
)(Stores);
