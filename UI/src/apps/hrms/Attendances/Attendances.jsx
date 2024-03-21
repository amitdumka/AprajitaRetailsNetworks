import React, { PureComponent } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
//import { Test } from './Attendances.styles';

class Attendances extends PureComponent { 
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  componentWillMount = () => {
    console.log('Attendances will mount');
  }

  componentDidMount = () => {
    console.log('Attendances mounted');
  }

  componentWillReceiveProps = (nextProps) => {
    console.log('Attendances will receive props', nextProps);
  }

  componentWillUpdate = (nextProps, nextState) => {
    console.log('Attendances will update', nextProps, nextState);
  }


  componentDidUpdate = () => {
    console.log('Attendances did update');
  }

  componentWillUnmount = () => {
    console.log('Attendances will unmount');
  }

  render () {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return (
      <div className="AttendancesWrapper">
        Test content
      </div>
    );
  }
}

Attendances.propTypes = {
  // bla: PropTypes.string,
};

Attendances.defaultProps = {
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
)(Attendances);
