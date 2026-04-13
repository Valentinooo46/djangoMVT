import React, { useState, useEffect } from 'react';
import { 
  useGetTrainsQuery, 
  useGetCarriagesQuery, 
  useEditTrainMutation, 
  useEditCarriageMutation 
} from '../features/api/apiSlice';

export default function TrainUnitsList() {
  const { data: trains = [], isLoading: trainsLoading, error: trainsError } = useGetTrainsQuery();
  const { data: carriages = [], isLoading: carriagesLoading, error: carriagesError } = useGetCarriagesQuery();

  const [selectedTrainId, setSelectedTrainId] = useState(null);
  const [selectedCarriageId, setSelectedCarriageId] = useState(null);

  const [trainForm, setTrainForm] = useState({
    departure: '',
    arrival: '',
    departure_time: '',
    arrival_time: ''
  });

  const [carriageForm, setCarriageForm] = useState({
    name: '',
    number: ''
  });

  const [updateTrain, { isLoading: isUpdatingTrain }] = useEditTrainMutation();
  const [updateCarriage, { isLoading: isUpdatingCarriage }] = useEditCarriageMutation();

  useEffect(() => {
    if (selectedTrainId) {
      const train = trains.find(t => t.id === selectedTrainId);
      if (train) {
        setTrainForm({
          departure: train.departure || '',
          arrival: train.arrival || '',
          departure_time: train.departure_time ? train.departure_time.slice(0, 16) : '',
          arrival_time: train.arrival_time ? train.arrival_time.slice(0, 16) : '',
        });
      }
    }
  }, [selectedTrainId, trains]);

  useEffect(() => {
    if (selectedCarriageId) {
      const carriage = carriages.find(c => c.id === selectedCarriageId);
      if (carriage) {
        setCarriageForm({
          name: carriage.name || '',
          number: carriage.number || '',
        });
      }
    }
  }, [selectedCarriageId, carriages]);

  const handleTrainChange = (e) => {
    const { name, value } = e.target;
    setTrainForm(prev => ({ ...prev, [name]: value }));
  };

  const handleCarriageChange = (e) => {
    const { name, value } = e.target;
    setCarriageForm(prev => ({ ...prev, [name]: value }));
  };

  const handleTrainSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateTrain({ id: selectedTrainId, ...trainForm }).unwrap();
      alert('Потяг оновлено');
      setSelectedTrainId(null);
    } catch {
      alert('Помилка оновлення потяга');
    }
  };

  const handleCarriageSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateCarriage({ id: selectedCarriageId, ...carriageForm }).unwrap();
      alert('Вагон оновлено');
      setSelectedCarriageId(null);
    } catch {
      alert('Помилка оновлення вагона');
    }
  };

  if (trainsLoading || carriagesLoading) return <p>Завантаження...</p>;
  if (trainsError) return <p>Помилка завантаження потягів: {trainsError.toString()}</p>;
  if (carriagesError) return <p>Помилка завантаження вагонів: {carriagesError.toString()}</p>;

  return (
    <div className="container mt-4">
      <h2>Вагони</h2>
      <ul className="list-group mb-3">
        {carriages.map(carriage => (
          carriage.name ? (
            <li key={carriage.id} className="list-group-item d-flex justify-content-between align-items-center">
              {carriage.name} ({carriage.number})
              <button className="btn btn-sm btn-primary" onClick={() => setSelectedCarriageId(carriage.id)}>
                Редагувати
              </button>
            </li>
          ) : null
        ))}
      </ul>

      <h2>Потяги</h2>
      <ul className="list-group mb-3">
        {trains.map(train => (
          train.name ? (
            <li key={train.id} className="list-group-item d-flex justify-content-between align-items-center">
              {train.name} ({train.number})
              <button className="btn btn-sm btn-primary" onClick={() => setSelectedTrainId(train.id)}>
                Редагувати
              </button>
            </li>
          ) : null
        ))}
      </ul>

      {selectedTrainId && (
        <div className="card p-3 mb-3">
          <h4>Редагування потяга ID: {selectedTrainId}</h4>
          <form onSubmit={handleTrainSubmit}>
            <div className="mb-3">
              <label className="form-label">Відправлення</label>
              <input
                type="text"
                name="departure"
                className="form-control"
                value={trainForm.departure}
                onChange={handleTrainChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Прибуття</label>
              <input
                type="text"
                name="arrival"
                className="form-control"
                value={trainForm.arrival}
                onChange={handleTrainChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Час відправлення</label>
              <input
                type="datetime-local"
                name="departure_time"
                className="form-control"
                value={trainForm.departure_time}
                onChange={handleTrainChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Час прибуття</label>
              <input
                type="datetime-local"
                name="arrival_time"
                className="form-control"
                value={trainForm.arrival_time}
                onChange={handleTrainChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-success" disabled={isUpdatingTrain}>Зберегти</button>
            <button type="button" className="btn btn-secondary ms-2" onClick={() => setSelectedTrainId(null)}>Скасувати</button>
          </form>
        </div>
      )}

      {selectedCarriageId && (
        <div className="card p-3 mb-3">
          <h4>Редагування вагона ID: {selectedCarriageId}</h4>
          <form onSubmit={handleCarriageSubmit}>
            <div className="mb-3">
              <label className="form-label">Назва</label>
              <input
                type="text"
                name="name"
                className="form-control"
                value={carriageForm.name}
                onChange={handleCarriageChange}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Номер</label>
              <input
                type="text"
                name="number"
                className="form-control"
                value={carriageForm.number}
                onChange={handleCarriageChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-success" disabled={isUpdatingCarriage}>Зберегти</button>
            <button type="button" className="btn btn-secondary ms-2" onClick={() => setSelectedCarriageId(null)}>Скасувати</button>
          </form>
        </div>
      )}
    </div>
  );
}