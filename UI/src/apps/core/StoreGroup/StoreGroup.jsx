import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './StoreGroup.styles';

class StoreGroup extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('StoreGroup will mount');
  }

  componentDidMount = () => {
    console.log('StoreGroup mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('StoreGroup will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('StoreGroup will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('StoreGroup did update');
  }

  componentWillUnmount = () => {
    console.log('StoreGroup will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="StoreGroupWrapper">
        Test content
      </div>
    );
  }
}

StoreGroup.propTypes = {
  // bla: PropTypes.string,
};

StoreGroup.defaultProps = {
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
)(StoreGroup);
